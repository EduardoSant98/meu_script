#!/bin/bash
read -p "Digite a operação (ex: 2+2, 2-2, 3*3, 3/3): " operacao
echo "Resultado: $(echo "$operacao" | bc)"

