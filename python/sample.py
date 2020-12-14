import datetime

def rotate_windows(vim):
    print(datetime.datetime.now())
    print(vim.current.window)
    print(vim.windows)
    #del vim.current.buffer[-1]
    print(vim.current.window.vars)
    print(vars(vim.current.window.vars))

    print("rotating")
