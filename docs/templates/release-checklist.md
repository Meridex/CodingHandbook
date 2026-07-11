# Release Checklist — vX.Y.Z

**Repository:** ___________________
**Release prepared by:** ___________________
**Date:** ___________________

---

## Before Tagging

- [ ] All planned features for this release are merged to `main`
- [ ] All tests pass on `main`
- [ ] CHANGELOG updated with release notes
- [ ] Version number bumped in code (`setup.cfg` / `pyproject.toml` / `CMakeLists.txt`)
- [ ] Documentation up to date
- [ ] No known blocking bugs

## Tagging

- [ ] Annotated tag created:
      ```bash
      git tag -a vX.Y.Z -m "Release vX.Y.Z — brief description"
      ```

- [ ] Tag pushed: `git push origin vX.Y.Z`
- [ ] Tag verified on GitHub

## GitHub Release

- [ ] Release created from tag on GitHub
- [ ] Release title: `vX.Y.Z — Brief description`
- [ ] Release notes written (new features, bug fixes, breaking changes)
- [ ] Assets attached if applicable

## If Paper-Linked

- [ ] Tag includes arXiv ID in message
- [ ] README citation section updated
- [ ] Zenodo deposit created and DOI recorded
- [ ] `CITATION.cff` updated

## After Release

- [ ] Announce to group
- [ ] Close corresponding milestone
