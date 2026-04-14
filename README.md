# PenCon - CLI Exploitation Toolkit

A command-line toolkit that automates common exploitation tasks such as reverse shell generation, payload encoding, and listener setup.

## Features
- Reverse shell generator
- Payload encoding
- Listener automation
- Cheatsheet access

## Usage

Generate shell:
pencon shell --ip 127.0.0.1 --port 4444 --type bash

Start listener:
pencon listen --port 4444

Encode payload:
pencon encode --type base64 --data "whoami"
