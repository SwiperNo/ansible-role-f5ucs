#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def generate_range(start, end, step):
    current = start
    result = []
    while current < end:
        result.append(current)
        current += step
    return result

def main():
    module = AnsibleModule(
        argument_spec=dict(
            start=dict(type='int', required=True),
            end=dict(type='int', required=True),
            step=dict(type='int', required=True),
        )
    )

    start = module.params['start']
    end = module.params['end']
    step = module.params['step']
    
    byte_range = generate_range(start, end, step)

    module.exit_json(changed=False, byte_range=byte_range)

if __name__ == '__main__':
    main()