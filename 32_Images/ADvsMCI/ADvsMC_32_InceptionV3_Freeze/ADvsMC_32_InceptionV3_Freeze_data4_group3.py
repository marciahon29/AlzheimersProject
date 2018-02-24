import numpy as np
import h5py as h5py
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense
from keras import applications, optimizers


# dimensions of our images.
img_width, img_height = 150, 150

train_data_dir = '../data_04/train'
validation_data_dir = '../data_04/validation'
nb_train_samples = 5120
nb_validation_samples = 1280
epochs = 125
batch_size = 40


def save_bottlebeck_features():
	np.random.seed(2929)
	
	model = applications.InceptionV3(weights='imagenet', include_top=True, input_shape=(150, 150, 3))
	print('Model loaded.')

	#initialise top model
	#top_model = Sequential()
	#top_model.add(Flatten(input_shape=vgg_model.output_shape[1:]))
	#top_model.add(Dense(256, activation='relu'))
	#top_model.add(Dropout(0.5))
	#top_model.add(Dense(1, activation='sigmoid'))

        #model = Model(inputs=vgg_model.input, outputs=top_model(vgg_model.output))

        model.trainable = True

        model.summary()

	# Total of 313 layers (312 and 313 are the top layers)
	# Therefore the groups are the following:
	# 0 --> 0
	# 1 --> [0:62]
	# 2 --> [63:124]
	# 3 --> [125:186]
	# 4 --> [187:248]
	# 5 --> [249:311]
	# always keep classification layers trainable
        #layer_count = 1
        for layer in model.layers[0:186]:
            layer.trainable = False
	    #print("Top: Layer is %d trainable" %layer_count)  
	    #layer_count = layer_count + 1

        model.summary()


        train_datagen = ImageDataGenerator(rescale=1. / 255)
        test_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            train_data_dir,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode='binary')

        validation_generator = test_datagen.flow_from_directory(
            validation_data_dir,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode='binary')

	sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

#optimizers.Adam(lr=1e-6)

	model.compile( loss = "sparse_categorical_crossentropy", #"binary_crossentropy", 
            optimizer = sgd, 
            metrics=['accuracy']
            )

#        model.compile(optimizer='rmsprop',
#            loss='binary_crossentropy', metrics=['accuracy'])

        history = model.fit_generator(
	    train_generator,
            steps_per_epoch=nb_train_samples // batch_size,
            epochs=epochs,
            validation_data=validation_generator,
            validation_steps=nb_validation_samples // batch_size,
            verbose=1)

        history_dict =  history.history

        #Plotting the training and validation loss
        history_dict = history.history
        loss_values = history_dict['loss']
        val_loss_values = history_dict['val_loss']
        epochs_0 = range(1, len(history_dict['acc']) + 1)
        plt.plot(epochs_0, loss_values, 'bo', label='Training loss')
        plt.plot(epochs_0, val_loss_values, 'b', label='Validation loss')
        plt.title('ADvsMC_32_InceptionV3_Freeze_data4_group3 - Training and validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        #plt.show()
	plt.savefig('ADvsMC_32_InceptionV3_Freeze_data4_group3_loss.png')
	plt.close()

        #Plotting the training and validation accuracy
        acc_values = history_dict['acc']
        val_acc_values = history_dict['val_acc']
        plt.plot(epochs_0, acc_values, 'bo', label='Training acc')
        plt.plot(epochs_0, val_acc_values, 'b', label='Validation acc')
        plt.title('ADvsMC_32_InceptionV3_Freeze_data4_group3 - Training and validation accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        #plt.show()
	plt.savefig('ADvsMC_32_InceptionV3_Freeze_data4_group3_acc.png')
	plt.close()


save_bottlebeck_features()


