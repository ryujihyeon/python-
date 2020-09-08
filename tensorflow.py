#%%
import tensorflow as tf 
print(f'version:{tf.__version__}')
# %%
print('gpu','사용가능' if tf.config.experimental.list_physical_devices("GPU")else "사용불가")
# %%
tensor_a = tf.constant(100)
print(tensor_a)
# %%
print(tensor_a.numpy())
# %%
tensor_b = tf.constant(3)
tensor_c = tf.constant(2)
tensor_d = tf.add(tensor_b,tensor_c)

print(tensor_d,numpy())

#%%
tensor_ma =tf.constant([1,2],[3,4])
tensor_mb =tf,constant([2,0],[0,2])
tensor_mc =tensor_ma *tensor_mb
print(tensor_mc.numpy())
#%%
import tensorflow as tf
import numpy as np

print(f'tf version {tf.__version__}')

#데이터셋 만들기 
_input =np.array([0,0],[0,1],[1,0],[1,1]).astype(np.float64)
_output =np.array([0],[1],[1],[0]).astype(np.float64)

train_dataset = tf.data.Dataset.from_tensor_slices((_input,_output))
test_dataset = tf.data.Dataset.from_tensor_slices((_input,_output))

BATCH_SIZE = 1

train_dataset = train_dataset.shuffle(4).batch(BATCH_SIZE)
train_dataset = train_dataset.batch(1)

#모델만들기 
def create_model() :
    layers = []
    layers.append(tf.keras.layers.Dense(2,activation= tf.nn.sigmoid))
    layers.append(tf.keras.layers.Dense(1,activation= tf.nn.sigmoid))
    model = tf.keras.Sequential(layers)
    print('layer setup')
    sgd = tf.keras.optimizer.SGD(lr=0.01, decay=0 , momentum=0.99,nesterov=True)
    model.compile (optimizer=sgd ,loss='mse' metrics =['mae,mse'])
    return model 

if __name__ == "__main__":
    model = create_model()
    model.fit(train_dataset, epochs =500, validation_data = test_dataset)
    print(model(_input))