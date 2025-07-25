# Python script to parse and extract firewall rules from config
def parse_firewall_rules(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line and ',' in line:
                rule = line.strip().split(': ')[-1]
                parts = rule.split(',')
                if len(parts) == 2:
                    direction, action = parts
                    print(f"Direction: {direction.strip()}, Action: {action.strip()}")

if __name__ == "__main__":
    parse_firewall_rules('data/sample_firewall_config.txt')
