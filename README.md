# timezone

Ansible role to install setup timezone,

## Installation

```yaml
   ansible-galaxy install zerodowntime.timezone
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
    - name: Ubuntu
      versions:
      - bionic
      - xenial
```

## Default role variables

| Variable name  | Required? |  Type  | Description                                |
|:-------------- |:---------:|:------:|:------------------------------------------ |
| timezone__name |    yes    | string | Name of the timezone for the system clock' |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:

      - role: zerodowntime.timezone
        timezone__name: 'UTC'
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
