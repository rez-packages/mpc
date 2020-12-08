name = "mpc"
version = "1.2.1"

requires=["mpfr-4.1.0+", "gmp-5.0.0+"]

variants=[["platform-linux", "arch-x86_64"]]

def commands():
    env.LD_LIBRARY_PATH="{root}/lib"


