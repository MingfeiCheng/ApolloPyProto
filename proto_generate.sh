#!/bin/bash

# Check if both arguments are provided
if [[ -z "$1" || -z "$2" ]]; then
    echo "Error: Missing required arguments."
    echo "Usage: $0 <APOLLO_PROTO_PATH> <APOLLO_PROTO_OUT_PATH>"
    exit 1
fi

# Assign parameters
APOLLO_PROTO_PATH="$1"
APOLLO_PROTO_OUT_PATH="$2"

echo "Using APOLLO_PROTO_PATH: $APOLLO_PROTO_PATH"
echo "Using APOLLO_PROTO_OUT_PATH: $APOLLO_PROTO_OUT_PATH"

# Find all .proto files, excluding .cache directories
find "$APOLLO_PROTO_PATH" -name '*.proto' | while read -r proto_file; do
    # Check if the file is inside a .cache directory
    if [[ "$proto_file" == *".cache"* ]]; then
        continue
    fi

    # Compile the .proto file
    protoc -I="$APOLLO_PROTO_PATH" --python_out="$APOLLO_PROTO_OUT_PATH" "$proto_file"
done
