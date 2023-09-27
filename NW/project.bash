echo aaaa
python recive.py &
file_path="info.txt"
echo 0 > $file_path
initial_size=$(wc -c < "$file_path")

# 파일이 비어있는 동안 계속 대기
while [ $initial_size -eq 2 ]; do
    echo "1sec stay"
    # 파일의 크기를 주기적으로 확인 (예: 10초마다)
    sleep 1
    
    # 파일의 크기를 다시 확인
    current_size=$(wc -c < "$file_path")
    
    # 초기 크기와 현재 크기가 다를 경우 파일에 무언가 쓰였다고 가정
    if [ $current_size -ne $initial_size ]; then
        echo "done"
        break
    fi
done

# 파일을 한 줄씩 읽어서 처리할 루프
cat info.txt

line_number=0
while IFS= read -r line; do
    line_number=$((line_number + 1))
    case $line_number in
        1) shape="$line" ;;
        2) flag="$line" ;;
        3) frame="$line" ;;
    esac
done < "$file_path"
python test.py $shape $flag $frame
python lee.py $shape $flag $frame &
# python jun.py $shape $flag $frame &