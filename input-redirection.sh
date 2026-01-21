#!/bin/bash

cat << 'EOF' > show-info.sh
#!/bin/bash

cat -e << end
The current directory is: $PWD
The default paths are: $PATH
The current user is: $USERNAME
end
EOF
