import ctypes

# Loading the kernel32.dll library
kernel32 = ctypes.WinDLL('kernel32.dll')

# Determine the types of arguments and return value of the GetSystemDirectoryW function
kernel32.GetSystemDirectoryW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint]
kernel32.GetSystemDirectoryW.restype = ctypes.c_uint

# Determine the types of arguments and return value of the GetWindowsDirectoryW function
kernel32.GetWindowsDirectoryW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint]
kernel32.GetWindowsDirectoryW.restype = ctypes.c_uint

# Determine the types of arguments and return value of the GetUserNameW function
kernel32.GetUserNameW.argtypes = [ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_uint)]
kernel32.GetUserNameW.restype = ctypes.c_uint

def get_system_directory():
     buffer_size = 260
     buffer = ctypes.create_unicode_buffer(buffer_size)
     result = kernel32.GetSystemDirectoryW(buffer, buffer_size)
     if result == 0:
         return "Failed to get system directory."
     else:
         return "Windows system directory:", buffer.value

def get_windows_directory():
     buffer_size = 260
     buffer = ctypes.create_unicode_buffer(buffer_size)
     result = kernel32.GetWindowsDirectoryW(buffer, buffer_size)
     if result == 0:
         return "Failed to get Windows directory."
     else:
         return "Windows directory:", buffer.value

def get_user_name():
     buffer_size = 260
     buffer = ctypes.create_unicode_buffer(buffer_size)
     size = ctypes.c_uint(buffer_size)
     result = kernel32.GetUserNameW(buffer, ctypes.byref(size))
     if result == 0:
         return "Failed to get username."
     else:
         return "Username:", buffer.value

# Calling new functions
print(get_system_directory())
print(get_windows_directory())
print(get_user_name())
