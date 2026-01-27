import sys, os

def main():
    if len(sys.argv) != 2 or not os.access(sys.argv[1], os.R_OK):
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as infile, open('out.txt', 'w') as outfile:
        for line in infile:
            if 'pineapple' in line:
                continue
            
            outfile.write(line)
        
if __name__ == "__main__":
    main()