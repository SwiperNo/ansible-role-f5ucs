# ansible-role-f5ucs

# Ansible Role for Backing Up UCS Files on BIG-IP Devices

## Overview

This Ansible role is designed to create a backup of the UCS (User Configuration Set) file from BIG-IP devices. It automatically handles all steps from initiating an API session to saving the UCS backup file on a utility server.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
  - [Ansible Requirements](#ansible-requirements)
  - [System Requirements](#system-requirements)
  - [Variable Requirements](#variable-requirements)
- [Role Logic](#role-logic)
- [Usage](#usage)
- [Debugging](#debugging)
- [License](#license)
- [Contributing](#contributing)
- [Author](#author)

## Requirements

### Ansible Requirements

- Ansible version: 2.9 or higher
- Ansible `uri` module for API interactions
- Ansible `assemble` module for file assembly
- `delegate_to` functionality must be available for task delegation

### System Requirements

- Control Node that can reach BIG-IP's API endpoint
- Utility server with NFS mount to store UCS files
- Python installed on the Ansible Control Node

### Variable Requirements

This role requires the following variables to be defined:

- `big_ip_address`: The IP address of the BIG-IP device.
- `bigip_username`: The username for the BIG-IP device.
- `bigip_password`: The password for the BIG-IP device.
- `tmp_dir`: Temporary directory to store UCS fragments on the control node.
- `nfs_mount_point`: NFS mount point where the complete UCS file will be stored.
- `chunk_size`: The size of each chunk during the file download (optional, default is set within the role).

## Role Logic

1. **Get Current Time**: Retrieves the current time to be used in naming the UCS file.
2. **Set Filename**: Sets the filename for the UCS backup.
3. **Initiate BIG-IP API Session**: Initializes a session with the BIG-IP API.
4. **Create UCS Backup**: Generates the UCS file on the BIG-IP device.
5. **Create Directory for Fragments**: Creates a directory to store file fragments.
6. **Fetch Initial Chunk of UCS**: Downloads the first chunk of the UCS file.
7. **Download Remaining Chunks**: Downloads the remaining chunks in parallel.
8. **Assemble File Parts**: Assembles all downloaded fragments to form the complete UCS file.
9. **Move Assembled UCS**: Moves the complete UCS file to a utility server.
10. **Clean Up**: Removes temporary files and directories.
11. **Delete UCS from BIG-IP**: Deletes the UCS file from the BIG-IP device post fetching.

## Usage
Include this role in your Ansible Playbook:

```yaml
- hosts: big_ip_servers
  roles:
    - name: your-role-name
```

## Debugging

Debug tasks are included within the role to help in troubleshooting. Look for lines starting with `=== IMPORTANT ===` and `=== ALERT ===` in the Ansible output for important messages.

## License

MIT

## Contributing

Contributions are welcome. Please submit pull requests for any enhancements.

## Author

Kyle Jones
