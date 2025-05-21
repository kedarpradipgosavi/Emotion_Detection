package com.example.facialrecognization;

import okhttp3.MultipartBody;
import okhttp3.ResponseBody;
import retrofit2.http.Multipart;
import retrofit2.http.POST;

public interface ApiService {
    @Multipart
    @POST("/analyze")
    Call<ResponseBody> uploadImage(@Part MultipartBody.Part image);
}
