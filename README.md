# GAN

Generative Adversarial Networks 관련 paper들과 해당 논문 review입니다. 



---

<span style='background-color: #E5EBF7;'> **GAN Basics** </span>

- GAN: Generative Adversarial Networks (2014) : [arxiv](https://arxiv.org/abs/1406.2661), [review](https://happy-jihye.github.io/gan/gan-1/) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/happy-jihye/GAN-Paper/blob/main/gan/1_GAN.ipynb)

- DCGAN: Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks (ICLR 2016)  : [arxiv](https://arxiv.org/abs/1511.06434), [review](https://happy-jihye.github.io/gan/gan-2/)

<span style='background-color: #E5EBF7;'> **Conditional GAN** </span>

- CGAN: Conditional Generative Adversarial Nets (2014) : [arxiv](https://arxiv.org/abs/1411.1784), [review](https://happy-jihye.github.io/gan/gan-3/)

- ACGAN: Conditional Image Synthesis With Auxiliary Classifier GANs (ICML 2017) : [arxiv](https://arxiv.org/abs/1610.09585), [review](https://happy-jihye.github.io/gan/gan-13/)

- **Pair Dataset** 

  - Pix2Pix: Image-to-Image Translation with Conditional Adversarial Networks (CVPR 2017) : [arxiv](https://arxiv.org/abs/1611.07004), [review](https://happy-jihye.github.io/gan/gan-8/)

  - SPADE: Semantic Image Synthesis with Spatially Adaptive Normalization (CVPR 2019) : [arxiv](https://arxiv.org/abs/1903.07291), [review](https://happy-jihye.github.io/gan/gan-9/)

- **Unpair Dataset** 

  - CycleGAN: Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (ICCV 2017) : [arxiv](https://arxiv.org/abs/1703.10593), [review](https://happy-jihye.github.io/gan/gan-10/)
  - FUNIT: Few-Shot Unsupervised Image-to-Image Translation (ICCV 2019) : [arxiv](https://arxiv.org/abs/1905.01723)
  - COCO-FUNIT: Few-Shot Unsupervised Image Translation with a Content Conditioned Style Encoder (ECCV 2020) : [arxiv](https://nvlabs.github.io/COCO-FUNIT/) 


- **Multi Domain**
  - BicycleGAN: Toward Multimodal Image-to-Image Translation (NIPS 2017) : [arxiv](https://arxiv.org/abs/1711.11586) 
  - StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation (CVPR 2018) : [arxiv](https://arxiv.org/abs/1711.09020), [review](https://happy-jihye.github.io/gan/gan-12/)
    - StarGAN v2: Diversity Image Synthesis for Multiple Domains (CVPR 2020) : [arxiv](https://arxiv.org/abs/1912.01865) 

  - MUNIT : Multi-Modal Unsupervised Image-to-Image Translation (ECCV 2018) : [arxiv](https://arxiv.org/abs/1804.04732), [review](https://happy-jihye.github.io/gan/gan-14/) 
  


<span style='background-color: #E5EBF7;'> **GAN Architecture** </span>

- Progressive GAN: Progressive Growing of GANs for Improved Quality, Stability, and Variation (ICLR 2018) : [arxiv](https://arxiv.org/abs/1710.10196), [review](https://happy-jihye.github.io/gan/gan-5/)

- StyleGAN: A Style-Based Generator Architecture for Generative Adversarial Networks (CVPR 2019) : [arxiv](https://arxiv.org/abs/1812.04948), [review](https://happy-jihye.github.io/gan/gan-6/)

  - StyleGAN2: Analyzing and Improving the Image Quality of StyleGAN (2020) : [arxiv](https://arxiv.org/abs/1912.04958), [review](https://happy-jihye.github.io/gan/gan-7/)
  
  - Training Generative Adversarial Networks with Limited Data (NeurlPS 2020) : [arxiv](https://arxiv.org/abs/2006.06676)  : review [#01](https://happy-jihye.github.io/gan/gan-19/), [#02](https://happy-jihye.github.io/gan/gan-20/) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/happy-jihye/GAN-Papers/blob/main/gan/StyleGAN2_ADA_Pytorch.ipynb)

- BigGAN: Large Scale GAN Training for High Fidelity Natural Image Synthesis (2019) : [arxiv](https://arxiv.org/abs/1809.11096) 


<span style='background-color: #E5EBF7;'> **Text-to-Image** </span>

- Generative Adversarial Text to Image Synthesis (ICML 2016) : [arxiv](https://arxiv.org/abs/1605.05396), [review](https://happy-jihye.github.io/gan/gan-4/)

- TediGAN: Text-Guided Diverse Face Image Generation and Manipulation (CVPR 2021) : [arxiv](https://arxiv.org/abs/2012.03308), [code](https://github.com/IIGROUP/TediGAN)

- StyleCLIP: Text-Driven Manipulation of StyleGAN Imagery (arXiv 2021) : [arxiv](https://arxiv.org/abs/2103.17249), [review](https://happy-jihye.github.io/gan/gan-15/)

<span style='background-color: #E5EBF7;'> **Improved Training Techniques** </span>

- SS-GAN: Self-Supervised GANs via Auxiliary Rotation Loss (CVPR 2019) : [paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Chen_Self-Supervised_GANs_via_Auxiliary_Rotation_Loss_CVPR_2019_paper.pdf), [review](https://happy-jihye.github.io/gan/gan-16/)

- CR-GAN: Consistency Regularization for Generative Adversarial Networks (ICLR 2020) : [arxiv](https://arxiv.org/abs/1910.12027), [review](https://happy-jihye.github.io/gan/gan-17/)

- ICR-GAN: Improved Consistency Regularization for GANs (AAAI 2021) : [arxiv](https://arxiv.org/abs/2002.04724), [review](https://happy-jihye.github.io/gan/gan-18/)

<span style='background-color: #E5EBF7;'> **GAN Inversion** </span>

1. **Latent Optimization**
   - Image2stylegan: How to embed images into the stylegan latent space? (ICCV 2019) : [arxiv](https://arxiv.org/abs/1904.03189), [review](https://happy-jihye.github.io/gan/gan-23/)
   - Image2stylegan++: How to edit the embedded images? (CVPR 2020) : [arxiv](https://arxiv.org/abs/1911.11544)
2. **Encoder**
   - ALAE: Adversarial latent autoencoders : [github](https://github.com/podgorskiy/ALAE)
   - pSp: Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation (CVPR 2021) : [arxiv](https://arxiv.org/abs/2008.00951), [review](https://happy-jihye.github.io/gan/gan-23/)
3. **Hybrid approach**
   - stylegan-encoder : [Github](https://github.com/pbaylies/stylegan-encoder)
   - IdInvert : In-Domain GAN Inversion for Real Image Editing (ECCV 2020) : [arxiv](https://arxiv.org/abs/2004.00049), [review](https://happy-jihye.github.io/gan/gan-23/)

<span style='background-color: #E5EBF7;'> **Disentangled Manipulation** </span>

- GANSpace: Discovering Interpretable GAN Controls (NeurIPS 2020) : [arxiv](https://arxiv.org/abs/2004.02546), [code](https://github.com/harskish/ganspace)
- GAN-Latent-Discovery: Unsupervised Discovery of Interpretable Directions in the GAN Latent Space (2020) : [arxiv](https://arxiv.org/abs/2002.03754), [code](https://github.com/anvoynov/GANLatentDiscovery)
- Editing in style: Uncovering the Local Semantics of GANs (CVPR 2020) : [arxiv](https://arxiv.org/abs/2004.14367), [code](https://github.com/IVRL/GANLocalEditing)
- InterFaceGAN Interpreting the Disentangled Face Representation Learned by GANs (TPAMI 2020) : [arxiv](https://arxiv.org/abs/2005.09635)
- CD3D: Cross-Domain and Disentangled Face Manipulation with 3D Guidance (2021) : [arxiv](https://arxiv.org/abs/2104.11228), [code](https://github.com/cassiePython/cddfm3d)
- StyleSpace: StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation (2021) : [arxiv](https://arxiv.org/abs/2011.12799), [code](https://github.com/xrenaa/StyleSpace-pytorch)


<span style='background-color: #E5EBF7;'> **Image Editing** </span>

- StyleCLIP: Text-Driven Manipulation of StyleGAN Imagery (arXiv 2021) : [arxiv](https://arxiv.org/abs/2103.17249), [review](https://happy-jihye.github.io/gan/gan-15/), [code](https://github.com/orpatashnik/StyleCLIP)
- sefa: Closed-Form Factorization of Latent Semantics in GANs (CVPR 2021) : [arxiv](https://arxiv.org/abs/2007.06600), [code](https://github.com/happy-jihye/Cartoon-StyleGAN)
- EigenGAN: Layer-Wise Eigen-Learning for GANs : [arxiv](https://arxiv.org/abs/2104.12476), [code](https://github.com/bryandlee/eigengan-pytorch)
- StyleMapGAN: Exploiting Spatial Dimensions of Latent in GAN for Real-time Image Editing (CVPR 2021) : [arxiv](https://arxiv.org/abs/2104.14754), [code](https://github.com/naver-ai/StyleMapGAN)
- SEAN: Image Synthesis with Semantic Region-Adaptive Normalization (CVPR 2020) : [arxiv](https://arxiv.org/abs/1911.12861), [code](https://github.com/ZPdesu/SEAN)




<span style='background-color: #E5EBF7;'> **Talking Head** </span>

- Few-Shot Adversarial Learning of Realistic Neural Talking Head Models (arxiv 2019) : [arxiv](https://arxiv.org/abs/1905.08233) : [review](https://happy-jihye.github.io/gan/gan-22/)
- Neural Head Reenactment with Latent Pose Descriptors (IEEE 2020) : [arxiv](https://arxiv.org/abs/2004.12000)  


---

## Reference 
- https://github.com/eriklindernoren/PyTorch-GAN
