import json

def extract_lut_info(json_file, output_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Get modules and cells
        modules = data.get('modules', {})
        
        for module_name, module_info in modules.items():
            f.write(f"Module: {module_name}\n")
            f.write("-" * 40 + "\n")

            # Get cells
            cells = module_info.get('cells', {})
            for cell_name, cell_info in cells.items():
                cell_type = cell_info.get('type')
                if cell_type.startswith('lut'):
                    f.write(f"Cell: {cell_name}\n")
                    f.write(f"  Type: {cell_type}\n")
                    
                    # Extract LUT configuration
                    connections = cell_info.get('connections', {})
                    for pin, conn in connections.items():
                        f.write(f"  {pin}: {conn}\n")
                    
                    # If LUT configuration contains a specific field, extract it
                    # Example: Assuming 'lut' cell type has a 'init' field for its configuration
                    lut_init = cell_info.get('attributes', {}).get('init')
                    if lut_init:
                        f.write(f"  LUT Initialization: {lut_init}\n")
                    f.write("\n")

if __name__ == "__main__":
    # File paths
    json_file = 'top.json'    # Input JSON file
    output_file = 'lut_info.txt' # Output file for LUT information
    
    # Extract LUT information
    extract_lut_info(json_file, output_file)
    print(f"Extracted LUT information to {output_file}")

