package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
    "strings"
	"encoding/hex"
	"crypto/aes"
	"crypto/cipher"
)

var (
	offset = []byte {0x59,0xc9,0x86,0xbb,0xf6,0x15,0xc1,0x27,0xe7,0x22}
)

func getData() string {
	fmt.Print("Input hex: ")
	reader := bufio.NewReader(os.Stdin)
	line, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	line = strings.ReplaceAll(line, "\r", "")
    line = strings.ReplaceAll(line, "\n", "")
	return line
}

func xorData(data []byte) []byte {
	xorKey := []byte{0x0d,0x15,0x5e,0x9a,0xa1,0xcc,0xf9}
	var hexArray []byte
	for i := 0; i < len(data); i++ {
		temp := data[i] ^ xorKey[(i*2)%len(xorKey)]
		hexArray = append(hexArray, temp)
	}
	return hexArray
}

func decodeDataAES(data []byte) []byte {
	tempKey := []byte{0x7c,0x15,0x0c,0xd7,0x35,0xcc,0x46,0x32,0xa1,0x2c,0x8a,0x39,0x9c,0x70,0xdb,0x80,0xb9,0x2c,0xaf,0x0d,0x2b,0xd3,0x58,0xfc,0xe7,0x99,0x48,0x85,0xb2,0xb1,0x52,0x96}
	var keyFinal []byte

	for i := 0; i < len(tempKey); i++ {
		temp1 := (tempKey[i] + offset[(i*3)%len(offset)]) % 0xff
		temp2 := temp1 ^ (offset[i%len(offset)] % 0x20)
		keyFinal = append(keyFinal, temp2)
	}

	c, err := aes.NewCipher(keyFinal)
	if err != nil {
		log.Fatal(err)
	}

	gcm, err := cipher.NewGCM(c)
	if err != nil {
		log.Fatal(err)
	}

	nonceSize := gcm.NonceSize()
	nonce, ctext := data[:nonceSize], data[nonceSize:]

	ptext, err := gcm.Open(nil, nonce, ctext, nil)
	if err != nil {
		log.Fatal(err)
	}

	return ptext
}

func main() {
	data := getData()
	hexData, err := hex.DecodeString(data)
	if err != nil {
		log.Fatal(err)
	}
	xoredData1 := xorData(hexData)
	decData := decodeDataAES(xoredData1)
	xoredData2 := xorData(decData)
	finalDecode := string(xoredData2)
	fmt.Println("Decoded: ", finalDecode)
}
