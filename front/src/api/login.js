import request from '@/utils/request'
import qs from 'qs';

export function login(data) {
  console.log(data)
  return request({
    url: '/login/access-token',
    method: 'post',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    data: qs.stringify(data)
  })
}

export function getInfo(token) {
  return request({
    url: '/login/info',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
