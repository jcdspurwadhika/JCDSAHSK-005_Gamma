# JCDSAHSK-005_Gamma Customer Return Prediction & Prioritization Based on Historical Behavior

Olist merupakan marketplace e-commerce di Brazil yang menghubungkan customer dengan berbagai seller dan produk. Dataset Olist menyediakan informasi mengenai customer, histori transaksi, produk yang dibeli, kategori produk, serta informasi terkait order.

Dalam bisnis e-commerce, terdapat customer yang hanya melakukan pembelian satu kali dan tidak kembali melakukan transaksi, sementara customer lainnya melakukan repeat purchase.

Retention activity seperti voucher, discount, atau promotional campaign memiliki biaya. Oleh karena itu, perusahaan perlu mengetahui customer mana yang berisiko tidak kembali melakukan transaksi agar retention treatment dapat diberikan secara lebih tepat sasaran.

Pada project ini, historical customer behavior digunakan untuk memahami pola pembelian customer dan membangun model yang dapat membantu mengidentifikasi kemungkinan customer tidak kembali melakukan pembelian dalam 180 hari ke depan.

Dataset Olist tidak memiliki explicit churn label karena customer tidak melakukan subscription cancellation yang dapat secara langsung menandakan churn. Oleh karena itu, churn pada project ini didefinisikan menggunakan customer purchasing behavior pada future prediction window sebagai proxy untuk customer non-return.
