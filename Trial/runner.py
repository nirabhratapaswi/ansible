import ansible_runner
import yaml
data = [
    {
        "hosts": "ubuntu@54.193.67.251",
        "tasks": [
            {
                "name": "Create new file",
                "shell": "touch hello_runner.txt; echo \"Hello World from yaml converter\" > hello_runner.txt;"
            }
        ]
    }
]

stream = file('/home/tardis/Desktop/Ansible/Trial/project/converted.yaml', 'w')
yaml.dump(data, stream)

# r = ansible_runner.run(private_data_dir='/home/tardis/Desktop/Ansible/Trial', playbook='touch-playbook.yaml')
r = ansible_runner.run(private_data_dir='/home/tardis/Desktop/Ansible/Trial', playbook='converted.yaml')
print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)