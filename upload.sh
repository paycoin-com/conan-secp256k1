# example build script... don't use this, make your own... 

### public urls contain the "conan/" path to indicate the conan api, vs other packages

export CONAN_UPLOAD="https://api.bintray.com/conan/paycoin-com/secp256k1"
export CONAN_USERNAME="paycoin-com"
export CONAN_LOGIN_USERNAME="paycoin"
export CONAN_CHANNEL="stable"
export CONAN_EXTERNAL_GIT_REF=

### todo: should take real args, not just env vars
python3 build.py
