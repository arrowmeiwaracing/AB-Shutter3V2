# It is a node that picks up AB-Shutter3's button event. 
This is the Node-RED's node.  
AB Shutter3 is the camera shutter button of Bluetooth.  
AB Shutter3 is sold at the Daiso as of November 2017.  
AB-Shutter3�̃{�^���C�x���g���擾����Node-RED�p�m�[�h�ł��B
AB Shutter3�{�^���͂Q�O�P�V�N���_�Ń_�C�\�[�Ŕ̔����Ă���J�����p�����[�g�V���b�^�[�{�^���ł��B

https://www.youtube.com/watch?v=8WlTP4Ix2uA  
![�}�P](./doc/z000.png)
![�}�P](./doc/z201.png)

** When translating, please translate from [Japanese] into [your own language]. **  

## �C���X�g�[��
���ӁI�@���A�v����Raspberry Pi��p�ł��B���A�v����Node-RED�p�̒ǉ�node�ł��B

���z�[���t�H���_�� /home/pi �Ƃ��Đ������܂��B

1. �z�[���z����.node-red �t�H���_�� nodes �t�H���_���쐬���܂�
2. Github����ZIP��clone�R�}���h�ȂǂŎ擾�����t�@�C���S�Ă�nodes�z���ɒu���܂�  
��j.node-red/nodes/AB-Shutter3V2
3. ���s�����K�v�ȃt�@�C���Ɏ��s����t���܂�  
cd .node-red/nodes/AB-Shutter3V2  
sudo chmod -R a+rwx keyaccess.py  
4. keyaccess.py�͒ǉ���python���C�u�������K�v�ł��̂ŃC���X�g�[�����܂�  
sudo pip install evdev  


## �ݒ�

### AB-Shutter3�̃y�A�����O
1. AB-Shutter3�̓d����ON���܂�
2. Raspbian GUI��ʏ㕔�c�[���o�[��bluetooth�A�C�R����I�сA  
Add Device���_�C�A���O��AB-Shutter3�I�������x���_�C�A���O��OK���܂�  
����x�y�A�����O����ƍċN�����Ă��ݒ�͊o���Ă��܂����AAB-Shutter3��ON���邽�тɐڑ����̃_�C�A���O���o�Ă��܂�

## Node-RED�ł̎g����

### bluetoothbutton�m�[�h��input�s���ɓK���Ȓl����͂���Ɠ����n�߂܂�  
![�}�P](./doc/z001.png)  

### msg.payload.code, mode, btn �ŁA�������{�^���Ə�Ԃ������悤�ɂ��Ă���܂�

#### �傫���{�^���iiOS�Ə����Ă���j�𒷉��������ꍇ  

![�}�S](./doc/z101.png)  
code: 115 �� mode���@1(push)��2(hold)��0(relese)  
�i�{�^����ʁFbtn=A�@�ł��j

#### �������{�^���iandroid�Ə����Ă���j�𒷉��������ꍇ  

![�}�S](./doc/z102.png)  
code: 28����������ibtn=X�ɂ��Ă���܂��j�A  
code: 115 �� mode���@1(push)��2(hold)��0(relese)  
�i�{�^����ʁFbtn=B�@�ł��j  
code: 28�������ďI���ibtn=X�ɂ��Ă���܂��j

#### �傫���{�^���������Ȃ��珬�����{�^���𒷉��������ꍇ  
![�}�S](./doc/z103_1.png)  
![�}�S](./doc/z103_2.png)  
code: 28 �� mode���@2(hold)  
�i�{�^����ʁFbtn=C�@�ł��j  
�i�s�v�ȃC�x���g�ɂ��Ă̓{�^����ʁFbtn=X�ɂ��Ă���܂��j  


## �Ō��
Node-RED core library�̃\�[�X�����ɍ쐬���Ă��܂��B
���̂��߁A���̃��C�Z���X�Ɠ��� Apache License Version 2.0 �ɂ��܂����B  
�ǂ����A���y���݂��������B
