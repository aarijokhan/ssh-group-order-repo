import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../(tabs)/index'; 
import GroupOrderScreen from '../(tabs)/group-order';
import ProfileScreen from '../(tabs)/profile'; 
import MarketplaceScreen from '../(tabs)/marketplace';
import CheckoutScreen from '../(tabs)/checkout-screen'; 

type Product = {
  id: string;
  name: string;
  price: number;
  category: string;
};

type RootStackParamList = {
  Home: undefined;
  'group-order': undefined;
  explore: undefined;
  profile: undefined;
  marketplace: undefined;
  Checkout: { cart: Product[]; total: string };
};

const Stack = createStackNavigator<RootStackParamList>();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="group-order" component={GroupOrderScreen} />
  <Stack.Screen name="profile" component={ProfileScreen} />
  <Stack.Screen name="marketplace" component={MarketplaceScreen} options={{ headerTitle: 'Marketplace' }}/>
  <Stack.Screen name="Checkout" component={CheckoutScreen} />
</Stack.Navigator>
    </NavigationContainer>
  );
}
