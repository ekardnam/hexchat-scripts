#!/bin/bash

SCRIPTS=(
  join-chans.py
  translate.py
)
HEXCHAT_DIR=~/.config/hexchat/addons
REINSTALL=0

install() {
  for script in ${SCRIPTS[@]}; do
    if [ ! -f "$HEXCHAT_DIR/$script" ]; then
      cp $script "$HEXCHAT_DIR/$script"
      echo "[+] Installed $script to $HEXCHAT_DIR/$script"
    else
      if (( REINSTALL )); then
        cp $script "$HEXCHAT_DIR/$script"
        echo "[+] Reinstalled $script to $HEXCHAT_DIR/$script"
      else
        echo "[+] $script already installed"
      fi
    fi
  done
}

while (( $# )); do
  case $1 in
    -r|--reinstall)
      REINSTALL=1
      ;;
  esac
  shift
done

install
