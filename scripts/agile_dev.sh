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
  tmux split-window -h -t beautiful
  
  tmux new-window -t beautiful -n work
  tmux split-window -h -t beautiful:1
  # tmux split-window -v -t beautiful:1.0
  # tmux split-window -v -t beautiful:1.1
  tmux send-keys -t beautiful:1.0 "cd agile-de; python manage.py runserver 8001" C-m
  # tmux send-keys -t beautiful:1.1 "paver elastic" C-m
  # tmux send-keys -t beautiful:1.3 "paver rqworker" C-m
fi

##
# Attach tmux session.
#
tmux select-window -t beautiful:0
tmux select-pane -t beautiful:0.0
tmux attach -t beautiful