import request from '@/utils/request'

export function GetCurrentUserInfo() {
  return request({
    url: '/user/me',
    method: 'get',
  })
}

export function UpdateCurrentUserInfo(data) {
  return request({
    url: '/user/me',
    method: 'put',
    data
  })
}
