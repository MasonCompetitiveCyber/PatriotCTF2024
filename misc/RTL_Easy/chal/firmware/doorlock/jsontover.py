import json

def json_to_verilog(json_file, verilog_file):
    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Open the Verilog file for writing
    with open(verilog_file, 'w') as f:
        # Get module information
        modules = data.get('modules', {})
        for module_name, module_info in modules.items():
            f.write(f"module {module_name} (\n")
            
            # Write module ports
            ports = module_info.get('ports', {})
            for port_name, port_type in ports.items():
                f.write(f"    {port_type} {port_name},\n")
            # Remove trailing comma from the last port line
            f.seek(f.tell() - 2, 0)
            f.write('\n')
            f.write(");\n\n")
            
            # Write cells (logic gates, etc.)
            cells = module_info.get('cells', {})
            for cell_name, cell_info in cells.items():
                cell_type = cell_info.get('type')
                connections = cell_info.get('connections', {})
                f.write(f"  {cell_type} {cell_name} (\n")
                for pin, conn in connections.items():
                    f.write(f"    .{pin}({conn}),\n")
                # Remove trailing comma from the last pin line
                f.seek(f.tell() - 2, 0)
                f.write('\n')
                f.write("  );\n")
            
            # Write connections
            f.write("\n")
            connections = module_info.get('connections', {})
            for signal, value in connections.items():
                f.write(f"  assign {signal} = {value};\n")
            
            # Close module
            f.write("\nendmodule\n")

if __name__ == "__main__":
    # File paths
    json_file = 'top.json'    # Input JSON file
    verilog_file = 'output.v' # Output Verilog file
    
    # Convert JSON to Verilog
    json_to_verilog(json_file, verilog_file)
    print(f"Converted {json_file} to {verilog_file}")

