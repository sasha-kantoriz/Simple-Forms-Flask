// webpack.config.js
const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  mode: 'development',
  entry: './assets/main.js',
  output: {
    filename: 'index-bundle.js',
    path: path.resolve(__dirname, './static')
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      // это будет применяться к файлам `.js`
      // А ТАКЖЕ к секциям `<script>` внутри файлов `.vue`
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      // это будет применяться к файлам `.css`
      // А ТАКЖЕ к секциям `<style>` внутри файлов `.vue`
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.(png|jpe?g|gif|webm|mp4|svg)$/,
        loader: "file-loader",
        options: {
          outputPath: "./img",
          esModule: false,
        },
      },
    ]
  },
  plugins: [
    // убедитесь что подключили плагин!
    new VueLoaderPlugin()
  ]
}