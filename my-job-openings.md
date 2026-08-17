---
layout: default
---

## Job Openings

Offered by [Scientific Data Reduction Team](http://szcompressor.org/tabs/team) at [MCS division](http://www.mcs.anl.gov), [Argonne National Laboratory](http://www.anl.gov)

**We are seeking self-motivated, outstanding postdoc researcher and/or intern students for the following projects. The opportunities will continue until filled. (posted date: 07/16/2021)**

### Opportunity 1: Optimizing Error-bounded Lossy Compression by Machine/Deep Learning for Large-scale HPC Applications
**(seeking both postdoc and intern students)**

**Contact**: Sheng Di, [sdi1@anl.gov](mailto:sdi1@anl.gov), [http://www.mcs.anl.gov/~shdi](http://www.mcs.anl.gov/~shdi)

**Description**: Today's scientific applications are producing extremely large volumes of data, which are causing serious issues including storage burden, I/O bottlenecks, communication bottlenecks, and insufficient memory. Error-controlled lossy compression has been recognized as one of the most efficient solutions to resolve the big scientific data issue. Existing state-of-the-art lossy compressors, however, are all developed based on fixed/static compression models or pipeline, which cannot adapt to diverse data characteristics and sophisticated user-requirements. In this project, we will develop a scalable dynamic data reduction framework, which can optimize lossy compression for various use-cases dynamically and efficiently. The key techniques include using ML/DL to explore the diverse correlations of high-dimensional science datasets, using ML/DL to identify the best-qualified data compression model dynamically, using ML/DL to optimize the parameter configurations of various compression methods, using ML/DL to denoise datasets and/or recovering missing features for reconstructed data.

We are seeking self-motivated and independent postdoc researchers with strong background on ML, system design, and coding skills (C/C++). The selected candidate will work closely with the SZ compression team at Argonne to develop the cutting-edge lossy compression libraries/tools practically for the scientific community. The SZ team ([http://szcompressor.org](http://szcompressor.org)) is the leading team in the error-bounded lossy compression domain. The flagship software - SZ has been verified as one of the best error-bonded lossy compressors in the community by many domain scientists independently. Joining SZ team will have exceptional opportunities to collaborate with top-tier scientists in different domains and use cutting-edge supercomputers (Aurora, Summit, etc.).

### Opportunity 2: Scalable Dynamic Scientific Data Reduction
**(seeking both postdoc and intern students)**

**Contact**: Sheng Di, [sdi1@anl.gov](mailto:sdi1@anl.gov), [http://www.mcs.anl.gov/~shdi](http://www.mcs.anl.gov/~shdi)

**Description**: Lossy compression is critical to the success of today's and future scientific discovery because of the extreme volumes of data produced by scientific applications or instruments. Existing error-bounded lossy compressors, however, suffer from two significant drawbacks: (1) they support only simple error controlling (such as absolute error bound) that does not match the user's requirements for preserving quantities of interest and features; and (2) existing general-purpose data compressors are developed based on static designs without adaptability to the diverse characteristics of application datasets.

The overarching goal of this project is to develop a scalable dynamic scientific data reduction (SDR) framework (and practical library/toolkit) that can automatically construct the best-qualified data reduction solution in terms of user requirements and dynamic data characteristics, significantly improving data reduction quality and performance over the existing general-purpose lossy compressors.

### Opportunity 3: Developing Ultra-fast Lossy Compressor for Large-scale HPC Applications
**(seeking one intern student)**

**Contact**: Sheng Di, [sdi1@anl.gov](mailto:sdi1@anl.gov), [http://www.mcs.anl.gov/~shdi](http://www.mcs.anl.gov/~shdi)

**Description**: Ultra-fast lossy compression is highly demanded by many of today's scientific applications and instrument data acquisition. For instance, because of the memory limitation, many scientific simulations and DNN algorithms require a memory footprint compression algorithm, which is expected to be super-fast to avoid introducing significant performance delay because of compression/decompression overhead.

In this project, we will 1) improve the efficiency of the lossy compressor's coding stage through customization based on the characteristics of the intermediate data, 2) create lightweight lossy compression pipelines by automatically selecting data approximation, quantization, and coding stages, and 3) generate progressive compression/decompression algorithms leveraging a multi-resolution approach.

---

### For the candidate postdoc appointee/researcher:

**Requirement:**
- Ph.D degree in computer science, data analytics, or a related discipline.
- Familiarity with machine learning to a certain extent. (being familiar with deep learning will be a plus)
- Strong code development skills with C/C++. (being proficient in Python or Java will be a plus)
- Familiarity with parallel environment (openMP, MPI). (being familiar with GPU will be a plus)
- Strong publication record
- Strong skill in written and oral communications.

**Preferred extra experience:**
- Good mathematics background
- Experience in development of large-scale parallel systems
- Familiarity with various data compression techniques

### For the candidate intern student:

**Requirement:**
- Ph.D candidate in computer science, data analytics, or a related discipline.
- Strong code development skills with C/C++. (being proficient in Python or Java will be a plus)
- Familiarity with parallel environment (openMP, MPI). (being familiar with GPU will be a plus)
- Strong publication record
- Strong skill in written and oral communications.

**Preferred extra experience:**
- Familiarity with machine learning. (being familiar with deep learning will be a plus)
- Good mathematics background
- Experience in development of large-scale parallel systems
- Familiarity with various data compression techniques

### Remark for 'strong publication record':
- **For postdoc:** at least 1 top conference paper (such as SC, ICS, HPDC, IPDPS, PPoPP, FAST, PACT, ICDE, KDD, MICRO), or multiple second-tier conference papers (such as CLUSTER, CCGRID, HiPC) (journal papers will be a plus)
- **For student:** 1~2 second-tier conference papers (such as CLUSTER, CCGRID, HiPC) (top conference paper or journal papers will be a nice plus)
