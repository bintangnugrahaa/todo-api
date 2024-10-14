const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: true, // Aktifkan HTTPS untuk dev server
    port: 8080, // Ganti dengan port yang ingin Anda gunakan
  },
})
