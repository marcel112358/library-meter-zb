docker build --tag library_meter_zb:0.1 .
docker run -itd -e TZ=Europe/Zurich --mount type=bind,source="$(pwd)/zb-library-data",target=/usr/src/app/zb-library-data library_meter_zb:0.1
