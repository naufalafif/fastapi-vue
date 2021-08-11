import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/users',
    method: 'get',
    params
  })
}


export function AddUser(data) {
  return request({
    url: '/users',
    method: 'post',
    data
  })
}