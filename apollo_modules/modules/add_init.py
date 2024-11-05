import os

def add_init_py(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if __init__.py exists in the current directory
        if "__init__.py" not in filenames:
            # Create an empty __init__.py file
            init_path = os.path.join(dirpath, "__init__.py")
            with open(init_path, "w") as init_file:
                init_file.write("")  # Empty file
            print(f"Created: {init_path}")

# Replace 'my_project' with the path to your project directory
add_init_py('/Users/mingfeicheng/Desktop/PhD/Github/dev/ApolloSim_private/apollo_sim/modules')
