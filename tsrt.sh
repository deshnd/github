check_background() {
    while true; do
        if [ $(ps -p $$ -o stat=) != "S" ]; then
            echo "Script running in background"
            exit
        fi
        sleep 1
    done
}
check_background
