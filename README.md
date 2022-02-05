# rllib-torch-maddpg
PyTorch implementation of MADDPG (Lowe et al.) in RLLib

Note that the Ray version is currently pinned to 1.5.2.


```bash
export prj_path=/Users/michaelguarino/repos/rllib-torch-maddpg
docker run -dit --mount type=bind,source="${prj_path}",target="/usr/src/app/rllib-torch-maddpg" rllibtorchmaddpg:test
```