echo $PATH | tr ':' '\n' | xargs -I {} find {} -maxdepth 1 -type f -perm '++x'
