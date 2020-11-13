##
# Activate virtualenv.
#
source ~/.envs/horst/bin/activate

##
# Initiate tmus session if not existing.
#
tmux has-session -t beautiful
if [ $? != 0 ]
then
  tmux new-session -s beautiful -n edit -d
  tmux split-window -h -t beautiful:0
  tmux split-window -v -t beautiful:0.0
  tmux send-keys -t beautiful:0.0 "cd sample-paper-en; python manage.py runserver 8001" C-m
  tmux send-keys -t beautiful:0.1 "sass --watch styles/sample.scss:sample-paper-en/theme/styles/sample-journal.css" C-m

fi

##
# Attach tmux session.
#
tmux select-window -t beautiful:0
tmux select-pane -t beautiful:0.0
tmux attach -t beautiful
