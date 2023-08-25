# Ansible - pdfgen

\=========

## Role Variables

______________________________________________________________________

| Variables                | Type   | Options                               | Defaults                            |
| ------------------------ | ------ | ------------------------------------- | ----------------------------------- |
| pdfgen_document_path:    | string | ---                                   | /home/{{ ansible_user }}/Documents/ |
| pdfgen_user:             | string | ---                                   | "{{ ansible_user }}"                |
| pdfgen_service_name:     | string | ---                                   | pdfgen.service                      |
| pdfgen_service_state:    | string | reloaded, restarted, started, stopped | started                             |
| pdfgen_service_enabled:  | bool   | false, true                           | true                                |
| pdfgen_package_state:    | string | present, absent, latest               | present                             |
| pdfgen_package:          | list   | ---                                   | ---                                 |
| pdfgen_pip_package_state | string | present, absent, latest               | present                             |
| pdfgen_pip_package       | list   | ---                                   | ---                                 |

## Dependencies

______________________________________________________________________

## Example Playbook

______________________________________________________________________

### Basic

```
- name: Import pdfgen Role
  hosts: all
  roles:
    - role: giftpilz0.desktop.pdfgen
```
