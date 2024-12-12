import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

type Product = {
  id: string;
  name: string;
  price: number;
  category: string;
};

export default function MarketplaceScreen() {
  const [products, setProducts] = useState<Product[]>([]);
  const [cart, setCart] = useState<Product[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [cartTotal, setCartTotal] = useState<number>(0);

  useEffect(() => {
    axios
      .get<Product[]>('http://10.115.206.210:8000/products')
      .then((response) => setProducts(response.data))
      .catch(() => Alert.alert('Error', 'Failed to load products.'));

    const fetchCart = async () => {
      const storedCart = await AsyncStorage.getItem('userCart');
      setCart(storedCart ? JSON.parse(storedCart) : []);
    };
    fetchCart();
  }, []);

  useEffect(() => {
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    setCartTotal(total);

    AsyncStorage.setItem('userCart', JSON.stringify(cart));
  }, [cart]);

  const addToCart = (product: Product) => {
    setCart((prevCart) => [...prevCart, product]);
    Alert.alert('Added to Cart', `${product.name} has been added to your cart.`);
  };

  const getCategories = () => {
    return [...new Set(products.map((product) => product.category))];
  };

  return (
    <View style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <Text style={styles.header}>Marketplace</Text>      
        <Text style={styles.subHeader}>Categories:</Text>
        <ScrollView horizontal contentContainerStyle={styles.categoryContainer} showsHorizontalScrollIndicator={false}>
          {getCategories().map((category) => (
            <TouchableOpacity
              key={category}
              style={[styles.categoryButton, selectedCategory === category && styles.selectedCategory]}
              onPress={() => setSelectedCategory(category === selectedCategory ? null : category)}
            >
              <Text style={styles.categoryText}>{category}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
        <Text style={styles.subHeader}>Products:</Text>
        {products
          .filter((product) => !selectedCategory || product.category === selectedCategory)
          .map((product) => (
            <View key={product.id} style={styles.productCard}>
              <Text style={styles.productName}>{product.name}</Text>
              <Text style={styles.productPrice}>£{product.price.toFixed(2)}</Text>
              <TouchableOpacity style={styles.addButton} onPress={() => addToCart(product)}>
                <Text style={styles.addButtonText}>Add to Cart</Text>
              </TouchableOpacity>
            </View>
          ))}
        {cart.length > 0 && (
          <View style={styles.cartContainer}>
            <Text style={styles.cartHeader}>Your Cart:</Text>
            {cart.map((item, index) => (
              <Text key={index} style={styles.cartItem}>
                {item.name} - £{item.price.toFixed(2)}
              </Text>
            ))}
            <Text style={styles.cartTotal}>Total: £{cartTotal.toFixed(2)}</Text>
          </View>
        )}
        <View style={styles.bottomSpacer} />
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: 'grey',
  },
  scrollContainer: {
    flexGrow: 1,
    padding: 16,
    backgroundColor: 'white',
  },
  bottomSpacer: {
    height: 100,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  subHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  categoryContainer: {
    flexDirection: 'row',
    marginBottom: 16,
  },
  categoryButton: {
    backgroundColor: 'silver',
    padding: 10,
    borderRadius: 8,
    marginRight: 8,
  },
  selectedCategory: {
    backgroundColor: 'orange',
  },
  categoryText: {
    fontSize: 14,
    color: 'black',
  },
  productCard: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
  },
  productName: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  productPrice: {
    fontSize: 14,
    marginBottom: 8,
  },
  addButton: {
    backgroundColor: 'orange',
    padding: 10,
    borderRadius: 8,
    alignItems: 'center',
  },
  addButtonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  cartContainer: {
    marginTop: 16,
    padding: 16,
    backgroundColor: '#e0e0e0',
    borderRadius: 8,
  },
  cartHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  cartItem: {
    fontSize: 14,
    marginBottom: 4,
  },
  cartTotal: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
});
