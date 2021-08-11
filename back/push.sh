#! /bin/bash

read -p 'Push Message ? ' message

git add . 
git commit . -m "$message"
git push origin master

echo "Push Success"%  
