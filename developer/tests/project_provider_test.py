from runtime.project.providers import FilesystemProjectProvider

provider = FilesystemProjectProvider()

print()

print("Python Files")

print("----------------")

for file in provider.python_files()[:10]:

    print(file)

print()

print("Markdown Files")

print("----------------")

for file in provider.markdown_files():

    print(file)