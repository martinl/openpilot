#!/usr/bin/env bash

export API_HOST=https://api.konik.ai/
export ATHENA_HOST=wss://athena.konik.ai

export SKIP_FW_QUERY=1
export FINGERPRINT="BYD_SEALION_7"

exec ./launch_chffrplus.sh
