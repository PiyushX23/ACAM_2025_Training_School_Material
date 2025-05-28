#!/bin/bash 

YEAR=2025
MONTHMIN=1
MONTHMAX=2
DAYMIN=10
DAYMAX=15
METOP=C


for ((MONTH=$MONTHMIN; MONTH <=$MONTHMAX ; MONTH++)); do
	MMONTH=$(printf "%02d" "$MONTH")
        NBDAYSINMONTH=$(cal $month $year | awk 'NF {DAYS = $NF}; END {print DAYS}')

	DDAYMIN=$(printf "%02d" "$DAYMIN")
	DDAYMAX=$(printf "%02d" "$DAYMAX")

	FILENAME="IASI_METOP${METOP^}_L2_CO_${YEAR}${MMONTH}[$DDAYMIN-$NBDAYSINMONTH]_ULB-LATMOS_ICDR_V6.7.1.nc"
	echo "Downloading: $FILENAME"

	curl --insecure "https://cds-espri.ipsl.fr/iasi${METOP,}l2/iasi_co/V6.7.1/$YEAR/$MMONTH/$FILENAME" -O

done



