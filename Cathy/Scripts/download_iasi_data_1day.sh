#!/bin/bash 

YEAR=2025
MONTH=1
DAY=15
METOP=C

MMONTH=$(printf "%02d" "$MONTH")
DDAY=$(printf "%02d" "$DAY")

echo "${YEAR}${MMONTH}${DDAY}"
echo "IASI/METOP${METOP^}"

#curl --insecure https://cds-espri.ipsl.fr/iasi"${METOP,}"l2/iasi_co/V6.7.1/$YEAR/$MMONTH/IASI_METOP"${METOP^}"_L2_CO_"${YEAR}${MMONTH}${DDAY}"_ULB-LATMOS_ICDR_V6.7.1.nc -O

