---
name: Documentation issue
about: Report issue related to the Launchpad documentation
title: ''
labels: ''
assignees: ''

body:
  - type: markdown
    attributes:
      value: |
        **Thanks for taking the time to report this issue!**
        We appreciate your input, and it will help us improve the documentation.

        Please provide an appropriate title at the top of this page.
  - type: checkboxes
  id: content
  attributes:
    label: Select an option
    description: Please let us know what issue you encountered with the documentation.
    options:
      - label: I couldn't find what I was looking for
      - label: I found the information, but it was incorrect
      - label: I found the information, but it was incomplete
      - label: I found the information, but it was confusing
      - label: I encountered a technical issue (e.g., broken link, image not loading)
  - type: textarea
    id: description
    attributes:
      label: Issue description
      description: |
        Please provide a detailed description of the issue:
        - What part of the documentation were you trying to use?
        - What did you expect to happen, and what actually happened?
        - Any error messages or screenshots you can provide would be very helpful.
    validations:
      required: true
---