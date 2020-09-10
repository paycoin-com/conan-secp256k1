from conans import ConanFile, AutoToolsBuildEnvironment, tools


class Secp256k1Conan(ConanFile):
    name = "secp256k1"
    version = "1.0"
    license = "MIT"
    channel = "stable"
    # author = "Erik Aronesty <erik@getvida.io>"
    author = "Paycoin <hello@paycoin.com>"
    url = "https://github.com/paycoin-com/conan-secp256k1.git"
    description = "Optimized C library for EC operations on curve secp256k1"
    topics = ("bitcoin", "cryptography", "elliptic curve")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    build_policy = "missing"

    def source(self):
        self.run("git clone https://github.com/bitcoin-core/secp256k1.git")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)

        with tools.chdir("secp256k1"):
            autotools.defines.append("USE_FIELD_INV_NUM")
            autotools.defines.append("USE_FIELD_5X52")
            autotools.defines.append("USE_FIELD_5X52_ASM")
            autotools.defines.append("USE_FIELD_10X26=1")
            autotools.defines.append("USE_FIELD_INV_BUILTIN=1")
            autotools.defines.append("USE_SCALAR_INV_BUILTIN=1")
            autotools.defines.append("USE_SCALAR_8X32=1")
            # autotools.defines.append("USE_ENDOMORPHISM=1")
            autotools.defines.append("ENABLE_MODULE_SCHNORR=1")

            with tools.environment_append(autotools.vars):
                self.run("./autogen.sh")

            autotools.configure(args=[
                # "--enable-benchmark"
                # "--enable-coverage"
                # "--enable-tests"
                # "--enable-openssl-tests"
                "--enable-experimental"
                # "--enable-exhaustive-tests"
                "--enable-endomorphism"
                # "--enable-ecmult-static-precomputation"
                "--enable-module-ecdh"
                "--enable-module-recovery"
                # "--enable-external-default-callbacks"
                # "--with-bignum=auto"
                # "--with-asm==auto"
                # "--with-ecmult-window=auto"
                # "--with-ecmult-gen-precision=auto"
            ])
            autotools.make()
            autotools.install()

    def package(self):
        self.copy("*.h", dst="include", src="secp256k1")
        self.copy("*secp256k1.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["secp256k1"]
