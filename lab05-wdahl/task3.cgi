#!/bin/bash_shellshock

echo "Content-type: text/plain"
echo
echo "****** Enviroment Varibales ******"
strings /proc/$$/environ