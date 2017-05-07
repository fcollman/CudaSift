if (CUDASIFT_WITH_LIB)
   set(
    CUDA_NVCC_FLAGS
    ${CUDA_NVCC_FLAGS};
    -O3 -gencode arch=compute_35,code=sm_35;
    )
  cuda_add_library(cudasift ${cuda_sources_absolute} SHARED)
  install(TARGETS cudasift DESTINATION lib)
endif()
