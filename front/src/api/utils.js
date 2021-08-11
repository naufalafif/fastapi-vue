import request from '@/utils/request'

export function UploadFile(formData) {
  return request({
    url: '/utils/uploadfile',
    method: 'post',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

