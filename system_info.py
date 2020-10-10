import platform
x = platform.uname()

print(f"system: {x.system}")
print(f"system: {x.node}")
print(f"system: {x.release}")
print(f"system: {x.version}")
print(f"system: {x.machine}")
print(f"system: {x.processor}")