
                #!/bin/bash
                export GENERATE_SOURCEMAP=false
                export NODE_OPTIONS="--max-old-space-size=4096"
                npm install
                npm run build
                